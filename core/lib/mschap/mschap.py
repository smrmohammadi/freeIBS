import des
import md4
import sha
import utils


def generate_nt_response_mschap(challenge,password):
    """
   NtChallengeResponse(
   IN  8-octet               Challenge,
   IN  0-to-256-unicode-char Password,
   OUT 24-octet              Response )
   {
      NtPasswordHash( Password, giving PasswordHash )
      ChallengeResponse( Challenge, PasswordHash, giving Response )
   }    
    """
    password_hash=nt_password_hash(password)
    return challenge_response(challenge,password_hash)


def generate_nt_response_mschap2(authenticator_challenge,peer_challenge,username,password):
    """
   GenerateNTResponse(
   IN  16-octet              AuthenticatorChallenge,
   IN  16-octet              PeerChallenge,

   IN  0-to-256-char         UserName,

   IN  0-to-256-unicode-char Password,
   OUT 24-octet              Response )
   {
      8-octet  Challenge
      16-octet PasswordHash

      ChallengeHash( PeerChallenge, AuthenticatorChallenge, UserName,
                     giving Challenge)

      NtPasswordHash( Password, giving PasswordHash )
      ChallengeResponse( Challenge, PasswordHash, giving Response )
   }
    
    """
    challenge=challenge_hash(peer_challenge,authenticator_challenge,username)
    password_hash=nt_password_hash(password)
    return challenge_response(challenge,password_hash)


def challenge_hash(peer_challenge,authenticator_challenge,username):
    """
   ChallengeHash(
   IN 16-octet               PeerChallenge,
   IN 16-octet               AuthenticatorChallenge,
   IN  0-to-256-char         UserName,
   OUT 8-octet               Challenge
   {

      /*
       * SHAInit(), SHAUpdate() and SHAFinal() functions are an
       * implementation of Secure Hash Algorithm (SHA-1) [11]. These are
       * available in public domain or can be licensed from
       * RSA Data Security, Inc.
       */

      SHAInit(Context)
      SHAUpdate(Context, PeerChallenge, 16)
      SHAUpdate(Context, AuthenticatorChallenge, 16)

      /*
       * Only the user name (as presented by the peer and
       * excluding any prepended domain name)
       * is used as input to SHAUpdate().
       */

      SHAUpdate(Context, UserName, strlen(Username))
      SHAFinal(Context, Digest)
      memcpy(Challenge, Digest, 8)
   }

    
    """
    sha_hash=sha.new()
    sha_hash.update(peer_challenge)
    sha_hash.update(authenticator_challenge)
    sha_hash.update(username)
    return sha_hash.digest()
    
def nt_password_hash(passwd):
    """
   NtPasswordHash(
   IN  0-to-256-unicode-char Password,
   OUT 16-octet              PasswordHash )
   {
      /*
       * Use the MD4 algorithm [5] to irreversibly hash Password
       * into PasswordHash.  Only the password is hashed without
       * including any terminating 0.
       */
    """

    # we have to have UNICODE password
    pw = utils.str2unicode(passwd)

    # do MD4 hash
    md4_context = md4.new()
    md4_context.update(pw)

    res = md4_context.digest()

    # addig zeros to get 21 bytes string
    res = res + '\000\000\000\000\000'

    return res


def challenge_response(challenge,password_hash):
    """
   ChallengeResponse(
   IN  8-octet  Challenge,
   IN  16-octet PasswordHash,
   OUT 24-octet Response )
   {
      Set ZPasswordHash to PasswordHash zero-padded to 21 octets

      DesEncrypt( Challenge,
                  1st 7-octets of ZPasswordHash,
                  giving 1st 8-octets of Response )

      DesEncrypt( Challenge,
                  2nd 7-octets of ZPasswordHash,
                  giving 2nd 8-octets of Response )

      DesEncrypt( Challenge,
                  3rd 7-octets of ZPasswordHash,
                  giving 3rd 8-octets of Response )
   }
    """
    zpassword_hash=password_hash
#    while len(zpassword_hash)<21:
#	zpassword_hash+="\0"
    
    response=""
    des_obj=des.DES(zpassword_hash[0:7])
    response+=des_obj.encrypt(challenge)

    des_obj=des.DES(zpassword_hash[7:14])
    response+=des_obj.encrypt(challenge)
    
    des_obj=des.DES(zpassword_hash[14:21])
    response+=des_obj.encrypt(challenge)
    return response
